# CH Video Downloader

### Script to download videos for your [Clone Hero](https://clonehero.net) songs automatically!

###### Project for studies in Python.

****

#### Project developed in [Python 3](https://python.org)

## Dependencies:

### [pytube](https://pytube.io)

```python
pip install pytube
```

#### *In the current version of pytube there is a bug when getting the video streams. To fix the bug, just look for the cipher.py file and replace line 30 with the command `var_regex = re.compile(r"^\$*\w+\W")`*
