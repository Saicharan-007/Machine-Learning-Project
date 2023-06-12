# Machine-Learning-Project


create conda environment

'''
conda create -p venv python==3.10.9 -y

''''
'''
conda activate venv/
'''

pip install -r requirements.txt

To add files to git
'''
git add .
or 
git add filename

'''
Note: To ignore file or folder from git we can write name of file/folder in .gitignore file

To check the git status
'''
git status
'''
To check all version maintained by git
'''
git log
'''
To create version/commit all changes by git
'''
git commit-m 'message'

''''
To send verion/changes to github
'''
git push origin main
'''

Build docker image
'''
docker build -t <image_name>:<tagname> .
''''
note:image name for docker image should be lower case

To list docker images
'''
docker images
'''

To run docker image
'''
docker run -p 5000:5000 -e PORT=5000 170f54bb93cd
'''
To check running container in docker
'''
docker ps
'''
To stop docker container
'''
docker stop <container_id>
'''

install ipynb kernal
'''
pip install ipynkernel
'''

