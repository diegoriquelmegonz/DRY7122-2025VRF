#!/bin/bash
tail -n 5 /etc/passwd > DRY-Linux-2025.txt
sudo chown root:root DRY-Linux-2025.txt
echo "informacion  de DRY-Linux-2025.txt:"
cat DRY-Linux-2025.txt
echo -e "\nPermisos del archivo:"
ls -l DRY-Linux-2025.txt
