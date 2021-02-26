#!/bin/bash
# sends a request to 0.0.0.0:5000/catch_me which will return the server's response
curl -s -L -H "Origin: HolbertonSchool" -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me

