from sys import version_info
from typing import List
import json


class Solution:
    def __init__(self, data_file_path: str, protocol_json_path: str):
        self.data_file_path = data_file_path
        self.protocol_json_path = protocol_json_path

        with open(self.data_file_path, "r") as f:
            self.data = f.readline()
        with open(self.protocol_json_path, "r") as f:
            self.protocols = json.load(f)

    # Question 1: What is the version name used in the communication session?
    def q1(self) -> str:

        parts = self.data.split(",")
        protocol_id = parts[2].strip()
        for version, info in self.protocols["protocols_by_version"].items():
            if protocol_id in info["protocols"]:
                return version
        return ""


    # Question 2: Which protocols have wrong messages frequency in the session compared to their expected frequency based on FPS?
    def q2(self) -> List[str]:
        version = self.q1()
        versions_info = self.protocols["protocols_by_version"][version]
        wrong_answer = []

        expected_fps = {
            36: 164,
            18: 84,
            9: 48,
            1:1
        }
        count = {}
        for l in self.data:
            parts = self.data.split(",")
            if len(parts) > 2:
                protocol_id = parts[2].strip().lower()
                count[protocol_id] = count.get(protocol_id,0)+1
                print(f"protocol id is: {protocol_id}, and the count is:{count[protocol_id]}")

        for proto in versions_info["protocols"]:
            if versions_info["id_type"] =="hex":
                protocol_id = proto.lower()
            else:
                protocol_id = hex(int(proto)).lower()

            if protocol_id in self.protocols["protocols"]:
                fps = self.protocols["protocols"][protocol_id]["fps"]
                expected = expected_fps[fps]

                if count.get(protocol_id,0)!=expected:
                    wrong_answer.append(protocol_id)

        return wrong_answer


    # Question 3: Which protocols are listed as relevant for the version but are missing in the data file?
    def q3(self) -> List[str]:
        pass

    # Question 4: Which protocols appear in the data file but are not listed as relevant for the version?
    def q4(self) -> List[str]:
        pass

    # Question 5: Which protocols have at least one message in the session with mismatch between the expected size integer and the actual message content size?
    def q5(self) -> List[str]:
        pass

    # Question 6: Which protocols are marked as non dynamic_size in protocol.json, but appear with inconsistent expected message sizes Integer in the data file?
    def q6(self) -> List[str]:
        pass


if __name__ == "__main__":
    data_file = "data.txt"
    protocol_file = "protocol.json"

    solution = Solution(data_file,protocol_file)

    print(solution.q1())
    print(solution.q2())
