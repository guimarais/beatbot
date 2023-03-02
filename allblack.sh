# lints all .py files with black
black *.py
#find . -name '*.py' -exec black {} \;
#ls '*.py' -exec black {} \;
#
pylint3 *.py
