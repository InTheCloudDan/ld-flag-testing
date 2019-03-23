# ld-flag-testing

Testing basic LaunchDarkly feature flagging. You will need to have your LaunchDarkly SDK key before running application.

It also expects 2 custom flags to be created `test-flag` and `internal-customers`.

- `test-flag` is a boolean flag.
- `internal-customers` is a string value. If you running on localhost and it is enabled you can see the secret button visiting: `http://127.0.0.1:5000/canary?customer_type=internal_qa`

To install:

```
git clone https://github.com/InTheCloudDan/ld-flag-testing.git
cd ld-flag-testing
pip install -r requirements.txt
```

To run, first export your SDK key then start application

```
export LD_KEY='replace_me'
python3 main.py
```
