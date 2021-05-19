# WriteUp

## AnimWiki

- LFI on post request
* `/proc/self/cmdline` => pythonapp.py
- Source code :
* `app.py`
- We have a comment :
* `#s3cr3t=5up3r_53cr3t_f7ag.txt`
- Access to the flag :
* `../5up3r_53cr3t_f7ag.txt`
- Double encode base64
* EPICTF{lfi_cAn_b3_dAn3r0u5}