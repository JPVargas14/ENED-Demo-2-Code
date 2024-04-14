# The following module allows for he genearation and output
# of a dictionary containing the name and number of zones of
# of each subtask in a demo. This includes the final track.

def GetSubtaskInfo():
    subtaskInfo = {'Subtask A': 6,'Subtask B': 3, 'Subtask C': 9, 'Final Track': 10 }

    return subtaskInfo

def GetSubtaskGradingColumns():
    subtaskGradingColumns = ["Team Number", "Subtask A Zones", "Subtask A Retry Zones", "Subtask B Zones", "Subtask B Retry Zones", 
                             "Subtask C Zones", "Subtask C Retry Zones", "Full Track Zones", " Full Track Retry Zones"]
    return subtaskGradingColumns