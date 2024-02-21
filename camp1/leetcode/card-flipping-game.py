class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        sets=set()
        db=set()
        df=set()
        for i in range(len(fronts)):
            if fronts[i]==backs[i]:
                sets.add(fronts[i])

        for i in range(len(fronts)):
            if fronts[i] not in sets:
                df.add(fronts[i])
            if backs[i] not in sets:
                db.add(backs[i])

        if len(df)>0 and len(db)>0:
            return min(min(db),min(df))
        elif len(df)>0:
            return min(df)
        elif len(db)>0:
            return min(db)
        else:
            return 0