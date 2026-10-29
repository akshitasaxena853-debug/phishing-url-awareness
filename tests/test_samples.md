
# Test Samples and Results

| Test | Sample | Expected result | Status |
|---|---|---|---|
| 1 | `https://www.example.com/login` | No listed warning signs | PASS |
| 2 | `http://192.0.2.10/account` | IP hostname and HTTP warnings | PASS |
| 3 | `http://example.com@sample.invalid/login` | @ symbol and HTTP warnings | PASS |
| 4 | `https://a.b.c.d.e.example.invalid/path` | Many hostname labels warning | PASS |
| 5 | `https://xn--example.invalid/` | Punycode marker warning | PASS |

These tests use example URLs and do not require visiting any website.
