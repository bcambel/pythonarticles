# Pip, VirtualEnv and VirtualEnvWrapper

[Pip](http://www.pip-installer.org/en/latest/) is the godfather of Python package index.

[VirtualEnv](http://www.virtualenv.org/en/latest/) is a tool to isolate your projects' dependencies from each other. Not only the pip will be controlled by virtualenv, you can also point a specific version of the Python.

[VirtualEnvWrapper](http://virtualenvwrapper.readthedocs.org/en/latest/) is a set of extensions to the **VirtualEnv**

So how does all ties together ? 

Let's start with virtualenv and pip

```bash
curl -O https://pypi.python.org/packages/source/v/virtualenv/virtualenv-1.9.1.tar.gz
tar xvfz virtualenv-1.9.1.tar.gz
cd virtualenv-1.9.1
sudo python setup.py install
```
This will install **VirtualEnv** from source, and will be globally available.

Once the installation is done, you are ready to use <code>virtualenv</code> on your terminal. You're now ready to begin with your new project.

