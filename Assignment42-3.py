import math
def ClaculateEucDistance(P1,P2):
    Ans=math.sqrt((P1["StudyHours"]-P2["StudyHours"]) **2 + (P1["Attendance"]-P2["Attendance"]) **2)
    return Ans

def main():
    Border="-"*40
    Data=[
        {"StudyHours":2,"Attendance":60,"Result":"Fail"},
        {"StudyHours":5,"Attendance":80,"Result":"Pass"},
        {"StudyHours":6,"Attendance":85,"Result":"Pass"},
        {"StudyHours":1,"Attendance":50,"Result":"Fail"}
    ]
    for i in Data:
        print(i)

    print(Border)

    StudyHours=int(input("Enter the StudyHours :"))
    Attendance=int(input("Enter the Attendance :"))

    new_point={"StudyHours":StudyHours,"Attendance":Attendance}
    print(Border)
    for d in Data:
        d["distance"]=ClaculateEucDistance(d,new_point)

    for d in Data:
        print("- Distance",d["distance"])
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
        label=neighbours["Result"]
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

    print("Final prediction is ",Name)

if __name__=="__main__":
    main()