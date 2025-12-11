media_type = input("What is the name of the file?").strip().lower()

if media_type.endswith('.gif'):
    print('image/gif')
elif media_type.endswith('.jpg') or media_type.endswith('.jpeg'):
    print('image/jpeg')
elif media_type.endswith('.png'):
    print('image/png')
elif media_type.endswith('.pdf'):
    print('application/pdf')
elif media_type.endswith('.txt'):
    print('text/plain')
elif media_type.endswith('.zip'):
    print('application/zip')
else:
    print('application/octet-stream')
