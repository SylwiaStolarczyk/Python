experience = 1
languages = ("python", "typescript", "javascript", "java")
contractType = "b2b"
if experience >=2 and "python" in languages and "java" in languages:
    if "b2b" in contractType or "employment" in contractType:
        print("kandydat przyjęty")
    else:
        print("kandydat nie jest przyjęty z powodu b2b")
else:
    print("nie jest przyjet bo exp i lang")