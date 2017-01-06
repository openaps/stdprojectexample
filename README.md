# stdprojectexample
Example and practice area for python releases.

## 0: Have a python package
There are several python packages that need your help.

#### Register python project

`python setup.py register`

### 1: Accrue consensus for release

Use peer review, and pull requests to your advantage.
Set up a `dev` branch to prepare all releases.  Create the first `dev` branch
immediately after the first release.  Immediately create a pull request from
`dev` into `master`.  Encourage people to create topical branches into the
`dev` branch.  When the `dev` branch is ready to be merged into to the master
branch, this signals the developers belief that the code included should be
used by default which creates a new release.

Make sure to "bump" the [version number](http://semver.io/) to create the first
commit needed to create a pull request.  In the initial development states,
ensure that the version number ends with the `-dev` label.

### 2: Release Dance

To create a new release of a python module, ensure the version number is
accurate according to http://semver.io/ in `setup.py`.

#### Merge to master
Merge the pull request either using the github merge button or using git on the
commandline from the `master` branch:

```
git checkout dev && git pull
git checkout master && git pull
git merge dev
```


At this point you have a git branch with everything needed for a release.
If using commandline instead of github pull request, ensure to close pull
request and delete `dev` branch on github.

#### Verify release

```
# Install locally as symlink
sudo python setup.py develop
# Install a copy as system package
sudo python setup.py install
# Should bring up a help page.
pydoc stdprojectexample
```

Run smoke tests.
```
# make test
# python setupd.py test
```
Update changelog.
We're about to create new commits.

#### Tag Release

Semver says the version will be `x.y.z`.  Ensure the version is accurate.  Edit
the `setup.py` file to ensure that the `-dev` label is removed, commit results.
Repeat verification steps.

```
git tag x.y.z
```
Git tag will allow you to add notes, changelog is recommended, citation of pull
requests is encouraged.

#### Publish Results

Transfering your results over a network link beyond your computer is indelible
and irreversible.  Any mistakes must be mitigated by another release.  A
release is a bell that cannot be unrung.

##### Push to PyPi

```
# Upload to PyPi
python setup.py build bdist_egg upload
```
Observe new release in pypi.

##### Push to Github

Push `master` branch along with all tags to github.
```
git push origin --tags master
```

Observe new release in Github.


### 3: Post Release

```
git branch -d dev
git checkout -b dev
# edit setup.py

```

Edit `setup.py` to bump the version number; according to semver, this would be
a patch release without any deltas, by default.

```
git commit -avm "init new development area"
git push -u origin dev
```

Create a new pull request on Github.

## Congratulations

Go tweet about your new release.
To install: `pip install -U stdprojectexample`.

To install an arbitrary (eg `dev`) version using pip without cloning the repo:
```
pip install -U http+https://github.com/openaps/stdprojectexample.git@dev
```

