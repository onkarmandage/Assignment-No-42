import math
def ClaculateEucDistance(P1,P2):
    Ans=math.sqrt((P1["X"]-P2["X"]) **2 + (P1["Y"]-P2["Y"]) **2)
    return Ans

def main():
    Border="-"*40
    Data=[
        {"point":"A","X":1,"Y":2,"Label":"Red"},
        {"point":"B","X":2,"Y":3,"Label":"Red"},
        {"point":"C","X":3,"Y":1,"Label":"Blue"},
        {"point":"D","X":6,"Y":5,"Label":"Blue"}
    ]
    for i in Data:
        print(i)

    print(Border)

    X=int(input("Enter the X coordinate :"))
    Y=int(input("Enter the Y coordinate :"))

    new_point={"X":X,"Y":Y}
    print(Border)
    for d in Data:
        d["distance"]=ClaculateEucDistance(d,new_point)

    for d in Data:
        print(d["point"],"- Distance",d["distance"])
    print(Border )
    sorted_data=sorted(Data,key=lambda item :item["distance"])
    print("Sorted data is ")
    for d in sorted_data:
        print(d)

    K=3
    nearest=sorted_data[:K]
    print(Border)
    print("Nearest 3 member are")
    print(Border)

    for d in nearest:
        print(d)
    print(Border)

    # voting
    votes={}

    for neighbours in nearest:
        label=neighbours["Label"]
        votes[label]=votes.get(label,0)+1

    print(Border)
    print("Voting result is ")
    print(Border)

    for d in votes:
        print("Name :",d,"Number of votes :",votes[d])

    print(Border)
    iMax=0
    Name=""
    for d in votes:
        if(votes[d]>iMax):
            iMax=votes[d]
            Name=d

    print("K =",K,"->",Name)

if __name__=="__main__":
    main()