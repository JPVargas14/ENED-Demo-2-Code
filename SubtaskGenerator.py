# The following module allows for he genearation and output
# of a dictionary containing the name and number of zones of
# of each subtask in a demo. This includes the final track.

def GetSubtaskInfo():
    subtaskInfo = {'Subtask A': 6,'Subtask B': 4, 'Subtask C': 9, 'Final Track': 11 }

    return subtaskInfo

def GetSubtaskGradingColumns():
    subtaskGradingColumns = ["Team Number", "Subtask A Zones", "Subtask B Zones", "Subtask C Zones", "Full Track Zones", 
                             "Subtask A Retry Zones", "Subtask B Retry Zones", "Subtask C Retry Zones"]
    return subtaskGradingColumns