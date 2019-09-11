# Developing locally

Here are some steps to develop this dependency locally and interact with source, interpreted from
https://confluence.twitter.biz/display/ENG/Overview%3A+Python+3rdparty+in+Source

1.  Create a git branch for this change.
2.  Edit `airflow/version.py` to change the version.
3.  Edit `source/3rdparty/python/BUILD` with the corresponding version.
4.  Run the command `python2.7 setup.py bdist_wheel` in the `airflow` directory to build the wheel.
    It will be written to `airflow/dist`.
5.  Clean out the pex cache: `rm -rf ~/.pex ~/.cache/pants`.
6.  Run `ps aux | grep pantsd` to find the pid of the pantsd process.
7.  Run `kill $pid` where `$pid` is the the pid just observed.
8.  From the `source` directory, run `./pants clean-all`.
9.  Now here are the hacky parts. The `run-local.sh` and `run-aurora.sh` all run pants commands
    without the option `--python-repos-repos`. You can either edit these to include this option,
    or run a pants command that includes it, which will cache the local artifact you need, e.g.
    `./pants test airflow:: --python-repos-repos="['file:///path/to/airflow/dist/', 'https://science-binaries.local.twitter.com/home/third_party/source/python/wheels/', 'https://science-binaries.local.twitter.com/home/third_party/source/python/bootstrap/','https://science-binaries.local.twitter.com/home/third_party/source/python/sources/']"`
10. Now you can start up airflow instances as usual with the newly built wheel!
11. See the above link for `Adding Dependencies to science-libraries`.
