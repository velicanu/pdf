import streamlit as st
from pikepdf import Pdf


def main():
    files = st.file_uploader("Choose files", type="pdf", accept_multiple_files=True)
    new = Pdf.new()
    for file_ in files:
        with Pdf.open(file_) as pdf:
            for page in pdf.pages:
                new.pages.append(page)
        print(file_)
    new.save("bar.pdf")
    with open("bar.pdf", "rb") as f:
        btn = st.download_button(
            label="Download merged pdf",
            data=f,
            file_name="merged.pdf",
            mime="application/pdf",
        )

    return "done"


if __name__ == "__main__":
    main()
