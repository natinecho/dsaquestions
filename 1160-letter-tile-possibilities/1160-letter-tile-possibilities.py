class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = Counter(tiles)

        def back():
            tot = 0
            for cc in count:
                if count[cc] > 0:
                    count[cc] -= 1
                    tot += (1 + back())
                    count[cc] += 1
            
            return tot

        return back()


        