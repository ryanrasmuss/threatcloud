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

