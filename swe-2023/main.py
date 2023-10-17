from preprocessing import preprocess_text

def main():
    # 예시 텍스트
    text = """
    여러 브랜드 수딩젤을 써봤지만 제형이 너무 부드럽고 촉촉해요.  
    특히 향이 너무 제 취향이에요. 아기한테 발라주기 전에 제가 먼저 
    발라봤는데 너무 촉촉하고 일단 향이 너무 좋아요. 
    지금도 리뷰 쓰는 내내 킁킁 하는 중이랍니다. 
    보습도 당연히 너무 좋고, 발랐을 때 깊숙히 흡수되는 느낌이에요. 
    끈적임 전혀 없어요. 조리원 퇴소할 때 선물로 받은 수딩젤은 
    너무 끈적여서 수딩젤이라는 느낌을 많이 못 받았었는데 디어비 
    수딩젤은 너무 촉촉하고 산뜻하고 향 너무 좋고 단점이란게 없네요. 
    특히 저희애는 피부에서 너무 건조한 느낌이 있는데 겨울에 로션 +
      크림 조합으로 발라주면 하루종일 저희 아기가 촉촉할 수 있을 거
        같아요 디어비 감사합니다.
    아쉬운 점이라면 대용량이 없다는 점. 좋은 제품이지만 단점이라면 
    작은 용량에 조금 비싼 금액인것 같아요. 좀 더 저렴하면 쟁겨두면서
      쓰고 싶은 수딩젤. 하지만 써볼수록 돈이 아깝지가 않을것 같아요.
    """
    
    new_text = preprocess_text(text)
    print(new_text)

if __name__ == "__main__":
    main()