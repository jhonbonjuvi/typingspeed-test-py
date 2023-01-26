import time 

# dinhe mag create ug function para sa processo
def test_type(variableName):
    print("Text kaba kasi type kita! boom! Type na!!!! \n")
    print(variableName)
    input("Please hit Enter para masugdan....")

    # declaring variables
    # e call ang object sa time
    time_start = time.time()
    typedText = input()
    end_time = time.time()
    

    time_mahuman =  end_time - time_start

    # gamitan ug split para ma tagsa and ma list
    length_word = typedText.split()
    forMinute = time_mahuman/60
    wordPerMinit = len(typedText.split)