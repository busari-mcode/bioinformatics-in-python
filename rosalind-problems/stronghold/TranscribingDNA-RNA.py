def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracial"""
    return seq.replace("T", "U")

print(transcription("GATGGAACTTGACTACGTAAATT"))