import math
from dataclasses import dataclass
from itertools import count, groupby
from functools import reduce
from typing import ClassVar
from operator import mul


@dataclass(slots=True)
class Point:
    x: int
    y: int
    z: int
    jb: int = -1

    _counter: ClassVar[count] = count()

    def distance(self, other: "Point") -> float:
        return math.sqrt(
            (self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2
        )

    @staticmethod
    def group_id() -> int:
        return next(Point._counter)

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

    @property
    def assigned(self) -> bool:
        return self.jb != -1

    @staticmethod
    def get_grouped_jbs(points: "list[Point]") -> list[int]:
        points.sort(key=lambda p: p.jb)
        jbs = [(jb, len(list(pts))) for jb, pts in groupby(points, lambda p: p.jb)]
        jbs.sort(key=lambda j: j[1])
        return list(reversed([j[1] for j in jbs]))


def main(data: str, max_circuts=10) -> int:
    points = Point.read_points(data)
    circuits = 0
    while circuits <= max_circuts and (
        to_process := list(filter(lambda x: not x.assigned, points))
    ):
        cur_point = to_process.pop()
        min_point, min_dist = None, float("inf")
        for point in to_process:
            dist = cur_point.distance(point)
            if dist and dist < min_dist:
                min_point, min_dist = point, dist

        for point in list(filter(lambda x: x.assigned, points)):
            dist = cur_point.distance(point)
            if dist and dist < min_dist:
                min_point, min_dist = point, dist

        if min_point:
            if min_point.assigned:
                cur_point.jb = min_point.jb
            else:
                cur_point.jb = Point.group_id()
                min_point.jb = cur_point.jb
            circuits += 1

    jbs = Point.get_grouped_jbs(list(filter(lambda p: p.assigned, points)))
    print(jbs[:3], reduce(mul, jbs[:3]))
    return reduce(mul, jbs[:3])


if __name__ == "__main__":
    assert (
        main(
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
        == 40
    )
