# Deep Path

For single image:
sudo docker run --rm -it -v <absolute-path-to-test-images>:/<mount_name> bioimaging/deep_path:latest -s <mount_name>/<imagefile> <model name>
(Eg.sudo docker run --rm -it -v /home/pmshiva/Documents/fastai/Gastro/Docker/new/msi:/images bioimaging/deep_path:latest -s images/MSS/im4.jpg msi)

For a group of images:
sudo docker run --rm -it -v <absolute-path-to-test-images>:/<mount_name> bioimaging/deep_path:latest -d <mount_name> <model name>
(Eg. sudo docker run --rm -it -v /home/pmshiva/Documents/fastai/Gastro/Docker/new/msi:/images bioimaging/deepp_path:latest -d images msi)
