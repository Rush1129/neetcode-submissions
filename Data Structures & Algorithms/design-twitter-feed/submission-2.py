class Twitter:
    def __init__(self):
        # userId -> list of [-cnt, tweetId]
        self.users = defaultdict(list)
        # followerId -> set of followeeIds
        self.follows = defaultdict(set)
        self.cnt = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.cnt += 1
        self.users[userId].append([-self.cnt, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        h = []
        # Add user's own tweets
        h.extend(self.users[userId])
        
        # Add tweets from followees
        for followeeId in self.follows[userId]:
            if followeeId != userId:
                h.extend(self.users[followeeId])
        
        # Min-heap based on negative count timestamp
        heapq.heapify(h)
        
        ans = []
        # Pop up to 10 most recent tweets
        while h and len(ans) < 10:
            ans.append(heapq.heappop(h)[1])
            
        return ans

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)