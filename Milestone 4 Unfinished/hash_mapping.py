from entry import Entry

class HashMapping():
    def __init__(self, size = 2):
        self.bucket_table = [[] for i in range(size)]
        self.size = size
        self.len = 0

    def _bucket(self, key):
        bucket_index = hash(key) % self.size
        bucket = self.bucket_table[bucket_index]
        return bucket

    def put(self, key, value):
        bucket = self._bucket(key)
        if self.__contains__(key):
            for entry in bucket:
                if entry.key == key:
                    entry.value = value
            return
        bucket.append(Entry(key, value))
        self.len += 1

        if self.len >= 2*self.size:
            self.rehash()

    def get(self, key):
        if not self.__contains__(key):
            raise KeyError()

        bucket = self._bucket(key)
        for entry in bucket:
            if key == entry.key:
                return entry.value

    def __contains__(self, key):
        bucket = self._bucket(key)
        for entry in bucket:
            if entry.key == key:
                return True
        return False
    
    def __len__(self):
        return self.len

    def rehash(self):
        old_buckets = self.bucket_table
        self.size *= 2
        self.bucket_table = [[] for i in range(self.size)]

        for bucket in old_buckets:
            for entry in bucket:
                self.bucket_table.put(entry.key, entry.value)





    