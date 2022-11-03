def  main():
    user = input("File name: ").strip().lower()
    check(user)


# def check(str):
#     if ".jpeg" in str:
#         print("image/jpeg")
#     elif ".gif" in str:
#         print("image/gif")
#     elif ".png" in str:
#         print("image/png")
#     elif ".txt" in str:
#         print("text/plain")
#     elif ".pdf" in str:
#         print("application/pdf")
#     elif ".zip" in str:
#         print("application/zip")
#     else:
#         print("application/octet-stream")



#using (endswith) string method
def check(str):
    if str.endswith(".jpg") or str.endswith(".jpeg"):
        print("image/jpeg")
    elif str.endswith(".pdf"):
        print("application/pdf")
    elif str.endswith(".txt"):
        print("text/plain")
    elif str.endswith(".png"):
        print("image/png")
    elif str.endswith(".gif"):
        print("image/gif")
    elif str.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")


main()