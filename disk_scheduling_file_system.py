class DiskScheduling:

    def fcfs(self, requests, head):
        sequence = requests
        movement = 0
        current = head

        for request in sequence:
            movement += abs(current - request)
            current = request

        return sequence, movement

    def sstf(self, requests, head):
        requests = requests.copy()
        sequence = []
        movement = 0
        current = head

        while requests:
            closest = min(requests, key=lambda x: abs(current - x))
            movement += abs(current - closest)
            current = closest
            sequence.append(closest)
            requests.remove(closest)

        return sequence, movement

    def cscan(self, requests, head, disk_size=200):
        left = sorted([x for x in requests if x < head])
        right = sorted([x for x in requests if x >= head])

        sequence = right + [disk_size - 1, 0] + left

        movement = 0
        current = head

        for request in sequence:
            movement += abs(current - request)
            current = request

        return sequence, movement

    def clook(self, requests, head):
        left = sorted([x for x in requests if x < head])
        right = sorted([x for x in requests if x >= head])

        sequence = right + left

        movement = 0
        current = head

        for request in sequence:
            movement += abs(current - request)
            current = request

        return sequence, movement

    def rss(self, requests, head):
        sequence = sorted(requests, key=lambda x: abs(x - head))

        movement = 0
        current = head

        for request in sequence:
            movement += abs(current - request)
            current = request

        return sequence, movement


class SimpleFileSystem:

    def __init__(self, total_blocks=20):
        self.total_blocks = total_blocks
        self.blocks = [None] * total_blocks
        self.directory = {}

    def create_file(self, name, data):
        if name in self.directory:
            print("File already exists.")
            return

        required = len(data)

        free_blocks = [
            i for i in range(self.total_blocks)
            if self.blocks[i] is None
        ]

        if len(free_blocks) < required:
            print("Not enough free blocks.")
            return

        allocated = free_blocks[:required]

        for block, value in zip(allocated, data):
            self.blocks[block] = value

        self.directory[name] = allocated

        print("File created successfully.")
        print("Allocated blocks:", allocated)

    def read_file(self, name):
        if name not in self.directory:
            print("File not found.")
            return

        data = []

        for block in self.directory[name]:
            data.append(self.blocks[block])

        print("File data:", data)

    def delete_file(self, name):
        if name not in self.directory:
            print("File not found.")
            return

        for block in self.directory[name]:
            self.blocks[block] = None

        del self.directory[name]

        print("File deleted successfully.")

    def show_directory(self):
        print("\nDirectory:")

        if not self.directory:
            print("Directory is empty.")
            return

        for name, blocks in self.directory.items():
            print(name, "-> Blocks:", blocks)

    def show_blocks(self):
        print("\nBlock Status:")

        for i, value in enumerate(self.blocks):
            if value is None:
                print(i, "-> Free")
            else:
                print(i, "->", value)


def main():

    print("DISK SCHEDULING")

    requests = [98, 183, 37, 122, 14, 124, 65, 67]
    head = 53

    disk = DiskScheduling()

    sequence, movement = disk.fcfs(requests, head)
    print("\nFCFS")
    print("Sequence:", sequence)
    print("Total Head Movement:", movement)

    sequence, movement = disk.sstf(requests, head)
    print("\nSSTF")
    print("Sequence:", sequence)
    print("Total Head Movement:", movement)

    sequence, movement = disk.cscan(requests, head)
    print("\nC-SCAN")
    print("Sequence:", sequence)
    print("Total Head Movement:", movement)

    sequence, movement = disk.clook(requests, head)
    print("\nC-LOOK")
    print("Sequence:", sequence)
    print("Total Head Movement:", movement)

    sequence, movement = disk.rss(requests, head)
    print("\nRSS")
    print("Sequence:", sequence)
    print("Total Head Movement:", movement)

    print("\n\nSIMPLE FILE SYSTEM")

    fs = SimpleFileSystem(20)

    fs.create_file("file1.txt", ["H", "E", "L", "L", "O"])

    fs.create_file("file2.txt", ["O", "S"])

    fs.show_directory()

    print("\nReading file1.txt:")
    fs.read_file("file1.txt")

    print("\nDeleting file1.txt:")
    fs.delete_file("file1.txt")

    fs.show_directory()

    fs.show_blocks()


if __name__ == "__main__":
    main()
