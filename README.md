# get_ip

This is an IP Address and System getter.

Adds the computer IP Address & System information to a log.txt file.
When the limit is reached (current limit is 40), it sends the file to the given email and starts over by overwriting log.txt.

**NOTE: This is only meant for educational purposes!**

Simple usage:

Clone:

```
git clone https://github.com/endormi/get_ip.git
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```python
python get_ip.py
```
