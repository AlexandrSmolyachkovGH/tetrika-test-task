def appearance(intervals: dict[str, list[int]]) -> int:
    lesson_start, lesson_end = intervals['lesson']

    def intervals_to_set(timestamps: list[int]) -> set[int]:
        presence = set()
        for i in range(0, len(timestamps), 2):
            start = max(timestamps[i], lesson_start)
            end = min(timestamps[i + 1], lesson_end)
            if start < end:
                presence.update(range(start, end))
        return presence

    pupil_presence = intervals_to_set(intervals['pupil'])
    tutor_presence = intervals_to_set(intervals['tutor'])

    return len(pupil_presence & tutor_presence)
