# First upload response

```json

{
  "response": {
    "status": {
      "code": 1002,
      "label": "UPLOAD_SUCCESS",
      "message": "The file was uploaded successfully."
    },
    "sha1": "7586b94e7b7e789395eecd3ff3a80c44b76160c1",
    "md5": "8f478b9eaa186c98e569da5889bcd82f",
    "sha256": "8b8dc07bd7897b4e95a987e0dcab920eb0baeaab2421a0255e60dce00cd0e487",
    "file_type": "",
    "file_name": "LoaderDemo4.xlsm",
    "features": [
      "te"
    ],
    "te": {
      "trust": 0,
      "images": [
        {
          "report": {
            "verdict": "unknown"
          },
          "status": "not_found",
          "id": "3ff3ddae-e7fd-4969-818c-d5f1a2be336d",
          "revision": 1
        },
        {
          "report": {
            "verdict": "unknown"
          },
          "status": "not_found",
          "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
          "revision": 1
        }
      ],
      "score": -2147483648,
      "status": {
        "code": 1002,
        "label": "UPLOAD_SUCCESS",
        "message": "The file was uploaded successfully."
      }
    }
  }
}
```

# Pending Response (still being emulated)

```json

{
    "response": {
      "status": {
        "code": 1003,
        "label": "PENDING",
        "message": "The request is pending."
      },
      "sha1": "7586b94e7b7e789395eecd3ff3a80c44b76160c1",
      "md5": "8f478b9eaa186c98e569da5889bcd82f",
      "sha256": "8b8dc07bd7897b4e95a987e0dcab920eb0baeaab2421a0255e60dce00cd0e487",
      "file_type": "",
      "file_name": "LoaderDemo4.xlsm",
      "features": [
        "te"
      ],
      "te": {
        "trust": 0,
        "images": [
          {
            "report": {
              "verdict": "unknown"
            },
            "status": "pending",
            "id": "3ff3ddae-e7fd-4969-818c-d5f1a2be336d",
            "revision": 1
          },
          {
            "report": {
              "verdict": "unknown"
            },
            "status": "pending",
            "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
            "revision": 1
          }
        ],
        "score": -2147483648,
        "status": {
          "code": 1003,
          "label": "PENDING",
          "message": "The request is pending."
        }
      }
    }
}
```

# Verdict Response BENIGN

```json

{
  "response": {
    "status": {
      "code": 1001,
      "label": "FOUND",
      "message": "The request has been fully answered."
    },
    "sha1": "7586b94e7b7e789395eecd3ff3a80c44b76160c1",
    "md5": "8f478b9eaa186c98e569da5889bcd82f",
    "sha256": "8b8dc07bd7897b4e95a987e0dcab920eb0baeaab2421a0255e60dce00cd0e487",
    "file_type": "",
    "file_name": "LoaderDemo4.xlsm",
    "features": [
      "te"
    ],
    "te": {
      "trust": 0,
      "images": [
        {
          "report": {
            "verdict": "benign"
          },
          "status": "found",
          "id": "3ff3ddae-e7fd-4969-818c-d5f1a2be336d",
          "revision": 1
        },
        {
          "report": {
            "verdict": "benign"
          },
          "status": "found",
          "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
          "revision": 1
        }
      ],
      "score": -2147483648,
      "combined_verdict": "benign",
      "status": {
        "code": 1001,
        "label": "FOUND",
        "message": "The request has been fully answered."
      }
    }
  }
}

```

# Verdict Response MALICIOUS

```json
{
  "response": [
    {
      "status": {
        "code": 1001,
        "label": "FOUND",
        "message": "The request has been fully answered."
      },
      "sha1": "586b5a65430263f62d656c96624967122568e274",
      "md5": "eefa6f98681d78b63f15d7e58934c6cc",
      "sha256": "653bc2b16b1624e045c1225810185e9aa3694dc378fe0095e2052b7f1e265d01",
      "file_type": "exe",
      "file_name": "Win32.WannaPeace.exe",
      "features": [
        "av",
        "te"
      ],
      "av": {
        "malware_info": {
          "signature_name": "Trojan.Win32.Ransomware.Win32.Wannapeace.TC.a",
          "malware_family": 312510,
          "malware_type": 114,
          "severity": 4,
          "confidence": 5
        },
        "status": {
          "code": 1001,
          "label": "FOUND",
          "message": "The request has been fully answered."
        }
      },
      "te": {
        "trust": 10,
        "images": [
          {
            "report": {
              "verdict": "malicious"
            },
            "status": "found",
            "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
            "revision": 1
          },
          {
            "report": {
              "verdict": "malicious"
            },
            "status": "found",
            "id": "3ff3ddae-e7fd-4969-818c-d5f1a2be336d",
            "revision": 1
          }
        ],
        "score": -2147483648,
        "combined_verdict": "malicious",
        "confidence": 3,
        "severity": 4,
        "status": {
          "code": 1001,
          "label": "FOUND",
          "message": "The request has been fully answered."
        }
      }
    }
  ]
}
```

# RESPONSE MALICIOUS WHERE IS PDF REPORT ID? HERE!
```json
200
{
  "response": {
    "status": {
      "code": 1001,
      "label": "FOUND",
      "message": "The request has been fully answered."
    },
    "sha1": "586b5a65430263f62d656c96624967122568e274",
    "md5": "eefa6f98681d78b63f15d7e58934c6cc",
    "sha256": "653bc2b16b1624e045c1225810185e9aa3694dc378fe0095e2052b7f1e265d01",
    "file_type": "",
    "file_name": "Win32.WannaPeace.exe",
    "features": [
      "te"
    ],
    "te": {
      "trust": 10,
      "images": [
        {
          "report": {
            "verdict": "malicious",
            "pdf_report": "67dcf393-18fa-4118-93c6-483720ba33af",
            "xml_report": "4f18319e-99da-43d5-bbdd-af51b791f58f"
          },
          "status": "found",
          "id": "3ff3ddae-e7fd-4969-818c-d5f1a2be336d",
          "revision": 1
        },
        {
          "report": {
            "verdict": "malicious",
            "pdf_report": "6942ca3f-61fc-49bc-a24f-54f34bc14530",
            "xml_report": "7b162f59-ac38-4113-99d3-49d5bab3a4c8"
          },
          "status": "found",
          "id": "e50e99f3-5963-4573-af9e-e3f4750b55e2",
          "revision": 1
        }
      ],
      "score": -2147483648,
      "combined_verdict": "malicious",
      "severity": 4,
      "confidence": 3,
      "status": {
        "code": 1001,
        "label": "FOUND",
        "message": "The request has been fully answered."
      }
    }
  }
}
```
