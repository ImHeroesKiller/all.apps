# Android Apps — Ary Wibowo

Katalog unduhan APK Android untuk seluruh proyek. Pilih kategori, aplikasi, lalu versi yang ingin diunduh.

| Kategori | Aplikasi | Katalog versi |
| --- | --- | --- |
| Keamanan & privasi | IDA Call Shield | [Semua versi](android/security/ida-call-shield/README.md) |

## Susunan katalog

Setiap aplikasi disusun sebagai `android/<kategori>/<nama-aplikasi>/`. Folder aplikasi memuat daftar versi, metadata paket dan tautan APK di GitHub Releases. Setiap versi memiliki folder dokumentasi sendiri di `versions/<versi>/`.

APK disimpan sebagai lampiran GitHub Releases agar dapat diunduh langsung tanpa login dan tidak membesarkan riwayat Git. Kode sumber dan kunci penandatanganan tetap di repositori proyek masing-masing.

## Konvensi

- Kategori: `security` (keamanan), `ai-assistants` (asisten AI), `business` (bisnis/operasional), `productivity` (produktivitas), atau `utilities` (utilitas).
- Nama file: `Nama-Aplikasi-v<versi>-<channel>.apk`, misalnya `IDA-Call-Shield-v2.1.0-UAT2.apk`.
- Tag rilis: `<nama-aplikasi>-v<versionName>`, misalnya `ida-call-shield-v2.1.0-uat2`.
- Setiap APK dicatat dengan package ID, versionName, versionCode, ukuran, SHA-256 file dan SHA-256 sertifikat penandatanganan.
- File versi lama tidak ditimpa. Jika isi berbeda pada versi yang sama, simpan sebagai varian build yang terpisah dengan checksum masing-masing.

APK UAT/RC merupakan paket pengujian. Gunakan versi terbaru yang ditunjuk pada halaman aplikasi untuk pengujian perangkat.
