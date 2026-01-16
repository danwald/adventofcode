import math
from dataclasses import dataclass


@dataclass(slots=True)
class Point:
    x: int
    y: int
    z: int
    jb: int = -1

    def distance(self, other: "Point") -> float:
        return math.sqrt(
            (self.x - other.x) ^ 2 + (self.y - other.y) ^ 2 + (self.z - other.z) ^ 2
        )

    @classmethod
    def point_str(cls, x: str, y: str, z: str) -> "Point":
        return cls(int(x), int(y), int(z))

    @classmethod
    def read_points(cls, point_data: str) -> "list[Point]":
        point_data = point_data.strip()
        points: "list[Point]" = []
        for line in point_data.split():
            points.append(cls.point_str(*line.split(",", 3)))
        return points

    def assigned(self) -> bool:
        return self.jb != -1


def main(data: str) -> int:
    points = Point.read_points(data)
    processed: list[Point] = []
    min_d = 0, min_point = None
    for point in points:
        if not point.assigned:
            dist = 
    return len(points)


if __name__ == "__main__":
    assert main(
        """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
    )
