
def prepare_bytes_for_transport(bytes_):
    return base64.b64encode(bytes_).decode(constants.STRING_ENCODING)

def unpack_bytes_from_transport(bytes_string):
    return base64.b64decode(bytes_string.encode(constants.STRING_ENCODING))