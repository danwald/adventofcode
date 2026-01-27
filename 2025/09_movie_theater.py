from dataclasses import dataclass


@dataclass(slots=True)
class Point:
    x: int
    y: int

    @classmethod
    def point_str(cls, x: str, y: str) -> "Point":
        return cls(int(x), int(y))

    @classmethod
    def read_points(cls, point_data: str) -> "list[Point]":
        point_data = point_data.strip()
        points: "list[Point]" = []
        for line in point_data.split():
            points.append(cls.point_str(*line.split(",", 3)))
        return points

    def area(self, other: "Point") -> int:
        return abs(self.x - other.x + 1) * abs(self.y - other.y + 1)

    @staticmethod
    def brute_force(points: "list[Point]") -> int:
        max_dist = 0
        for p1 in points:
            for p2 in points:
                max_dist = max(max_dist, p1.area(p2))
        return max_dist


def main(data, **_) -> int:
    points = Point.read_points(data)
    return Point.brute_force(points)


if __name__ == "__main__":
    assert (
        main(
            """7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""
        )
        == 50
    )
