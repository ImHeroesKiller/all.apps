#!/usr/bin/env python3
"""Verify public release APK sizes and SHA-256 against every application catalog."""
import hashlib,json,os,sys,urllib.request
from pathlib import Path
REPO='ImHeroesKiller/all.apps'
def get(url):
 headers={'User-Agent':'all.apps-catalog-verifier','Accept':'application/vnd.github+json'}
 token=os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
 if token and url.startswith('https://api.github.com/'):headers['Authorization']='Bearer '+token
 return urllib.request.urlopen(urllib.request.Request(url,headers=headers),timeout=60)
def verify(root):
 releases=[];page=1
 while True:
  with get(f'https://api.github.com/repos/{REPO}/releases?per_page=100&page={page}') as response:rows=json.load(response)
  releases.extend(rows)
  if len(rows)<100:break
  page+=1
 by_tag={row['tag_name']:row for row in releases};checked=0
 for path in sorted(root.glob('android/*/*/catalog.json')):
  catalog=json.loads(path.read_text());seen=set()
  for row in catalog['versions']:
   identity=(row['version_name'],row['version_code']);assert identity not in seen,identity;seen.add(identity)
   release=by_tag.get(row['tag']);assert release and not release['draft'],f'Missing release: {row["tag"]}'
   asset=next((x for x in release['assets'] if x['name']==row['filename']),None);assert asset,f'Missing APK: {row["filename"]}'
   assert asset['size']==row['size_bytes'],f'Size mismatch: {row["filename"]}'
   assert asset['browser_download_url']==row['download_url'],f'URL mismatch: {row["filename"]}'
   digest=asset.get('digest')
   if not digest:
    h=hashlib.sha256()
    with get(row['download_url']) as response:
     while chunk:=response.read(1024*1024):h.update(chunk)
    digest='sha256:'+h.hexdigest()
   assert digest=='sha256:'+row['sha256'],f'Checksum mismatch: {row["filename"]}'
   assert any(x['name']=='SHA256SUMS.txt' for x in release['assets']),f'Missing checksum file: {row["tag"]}'
   metadata=json.loads((path.parent/'versions'/row['version_name']/'metadata.json').read_text());assert metadata==row,f'Catalog metadata mismatch: {row["tag"]}'
   print('PASS',row['tag']);checked+=1
  latest=next(row for row in catalog['versions'] if row['version_name']==catalog['latest_version'])
  assert latest['download_url']==catalog['latest_download_url']
 print(f'PASS {checked} APK versions: public releases, exact sizes, checksums, URLs and metadata')
 return checked
if __name__=='__main__':
 try:verify(Path(__file__).resolve().parents[1])
 except Exception as e:print('FAIL',e,file=sys.stderr);sys.exit(1)
