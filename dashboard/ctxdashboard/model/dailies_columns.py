from ctxdashboard.util.listable_string_enum import ListableStringEnum


class DailiesColumns(ListableStringEnum):
    USER_LAST_NAME = "Tracker ID"
    DAILY_DURATION_S = "Computed daily duration (s)"
    START_DT = "Day start (timestamp)"
    END_DT = "Day end (timestamp)"