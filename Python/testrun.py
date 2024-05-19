
def translate_error_code(error_code):
 
    if error_code == "401 Unauthorized":
        translation = "Server received an unauthenticated request"
 
    elif error_code == "404 Not Found":
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":
        translation = "Server request to close unused connection"
 
    else:
        translation = "Unknown error code"
    return translation

print(translate_error_code("404 Not Found"))

# Outputs Requested web page not found on server