class HanoiTower:
    def __init__(self, num_disks):
        self.num_disks = num_disks
        self.towers = {
            1: list(range(num_disks, 0, -1)),
            2: [],
            3: []
        }

    def move(self, num_disks, source, target, auxiliary):
        if num_disks == 1:
            disk = self.towers[source].pop()
            self.towers[target].append(disk)
            print(f"Move disk {disk} from tower {source} to tower {target}")
        else:
            self.move(num_disks - 1, source, auxiliary, target)
            self.move(1, source, target, auxiliary)
            self.move(num_disks - 1, auxiliary, target, source)

    def solve(self):
        self.move(self.num_disks, 1, 3, 2)

# Test the HanoiTower class
if __name__ == "__main__":
    num_disks = 3
    hanoi = HanoiTower(num_disks)
    hanoi.solve()
