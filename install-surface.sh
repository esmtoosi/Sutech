#!/bin/bash
set -e

echo "➤ اضافه کردن مخزن linux-surface و کلیدها"
curl -s https://raw.githubusercontent.com/linux-surface/linux-surface/master/pkg/keys/surface.asc | gpg --dearmor | sudo tee /usr/share/keyrings/linux-surface.gpg > /dev/null
echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/linux-surface.gpg] https://pkg.surfacelinux.com/debian release main' | sudo tee /etc/apt/sources.list.d/linux-surface.list

echo "➤ آپدیت مخازن"
sudo apt update

echo "➤ نصب کرنل و headers surface"
sudo apt install -y linux-image-surface linux-headers-surface

echo "➤ نصب iptsd"
sudo apt install -y iptsd

echo "➤ تنظیم سرویس iptsd برای استفاده از /dev/mei0"
sudo bash -c 'cat > /etc/systemd/system/iptsd.service <<EOF
[Unit]
Description=Intel Precise Touch & Stylus Daemon
After=network.target

[Service]
ExecStart=/usr/bin/iptsd -d /dev/mei0
Restart=always
RestartSec=3
User=root

[Install]
WantedBy=multi-user.target
EOF'

sudo systemctl daemon-reload
sudo systemctl enable --now iptsd

echo "➤ دانلود firmware از github"
git clone https://github.com/linux-surface/linux-surface.git
sudo mkdir -p /lib/firmware/ipts
sudo cp linux-surface/firmware/ipts/* /lib/firmware/ipts/

echo "➤ آپدیت initramfs"
sudo update-initramfs -u

echo "➤ نصب کامل انجام شد. لطفاً سیستم را ریبوت کنید."
