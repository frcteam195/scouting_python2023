import statistics

def pit(analysis, rsRobotMatchData, rsRobotL2MatchData, rsRobotPitData):
    rsCEA = {}
    rsCEA['analysisTypeID'] = 40

    # print(rsRobotPitData)
    for pitData in rsRobotPitData:
        rsCEA['team'] = pitData[analysis.pitColumns.index('team')]
        rsCEA['eventID'] = pitData[analysis.pitColumns.index('eventID')]

        scoutingStatus = pitData[analysis.pitColumns.index('scoutingStatus')]
        # scoutingStatus: 3=finished, 2=finish later, 1=actively working on it, 0=nothing done
        if scoutingStatus == 3 or scoutingStatus == 2:  
            
            robotLengthValue = pitData[analysis.pitColumns.index('robotLength')]
            if robotLengthValue is None:
                robotLengthValue = 0
                robotLengthDisplay = '-'
            else:
                robotLengthDisplay = robotLengthValue
            rsCEA['M1D'] = str(robotLengthDisplay)
            rsCEA['M1V'] = robotLengthValue
            rsCEA['M1F'] = 0
            
            robotWidthValue = pitData[analysis.pitColumns.index('robotWidth')]
            if robotWidthValue is None:
                robotWidthValue = 0
                robotWidthDisplay = '-'
            else:
                robotWidthDisplay = robotWidthValue
            rsCEA['M2D'] = str(robotWidthDisplay)
            rsCEA['M2V'] = robotWidthValue
            rsCEA['M2F'] = 0

            robotHeightValue = pitData[analysis.pitColumns.index('robotHeight')]
            if robotHeightValue is None:
                robotHeightValue = 0
                robotHeightDisplay = '-'
            else:
                robotHeightDisplay = robotHeightValue
            rsCEA['M3D'] = str(robotHeightDisplay)
            rsCEA['M3V'] = robotHeightValue
            rsCEA['M3F'] = 0
            
            # robotWeightValue = pitData[analysis.pitColumns.index('robotWeight')]
            robotWeightValue = 99
            if robotWeightValue is None:
                robotWeightValue = 0
                robotWeightDisplay = '-'
            else:
                robotWeightDisplay = robotWeightValue
            rsCEA['M4D'] = str(robotWeightDisplay)
            rsCEA['M4V'] = robotWeightValue
            rsCEA['M4F'] = 0
            
            driveMotorTypeID = pitData[analysis.pitColumns.index('driveMotorTypeID')]
            if driveMotorTypeID is None:
                driveMotorTypeDisplay = '-'
            elif driveMotorTypeID == 0:
                driveMotorTypeDisplay = 'Falcon'
            elif driveMotorTypeID == 1:
                driveMotorTypeDisplay = 'NEO'
            elif driveMotorTypeID == 2:
                driveMotorTypeDisplay = 'NEO550'
            elif driveMotorTypeID == 3:
                driveMotorTypeDisplay = 'CIM'
            elif driveMotorTypeID == 4:
                driveMotorTypeDisplay = 'miniCIM'
            elif driveMotorTypeID == 5:
                driveMotorTypeDisplay = 'other'
            else:
                driveMotorTypeDisplay = '999'
            rsCEA['M5D'] = str(driveMotorTypeDisplay)
            rsCEA['M5V'] = driveMotorTypeID
            rsCEA['M5F'] = 0

            driveBaseTypeID = pitData[analysis.pitColumns.index('driveBaseTypeID')]
            if driveBaseTypeID is None:
                driveBaseTypeDisplay = '-'
            elif driveBaseTypeID == 0:
                driveBaseTypeDisplay = 'swerve'
            elif driveBaseTypeID == 1:
                driveBaseTypeDisplay = 'tank-4w'
            elif driveBaseTypeID == 2:
                driveBaseTypeDisplay = 'tank-6w'
            elif driveBaseTypeID == 3:
                driveBaseTypeDisplay = 'tank-8w'
            elif driveBaseTypeID == 4:
                driveBaseTypeDisplay = 'mecanumn'
            elif driveBaseTypeID == 5:
                driveBaseTypeDisplay = 'other'
            else:
                driveBaseTypeDisplay = '999'
            rsCEA['M6D'] = str(driveBaseTypeDisplay)
            rsCEA['M6V'] = driveBaseTypeID
            rsCEA['M6F'] = 0

            buildQualityValue = pitData[analysis.pitColumns.index('buildQuality')]
            if buildQualityValue is None:
                buildQualityValue = 0
                buildQualityDisplay = '-'
            if 1 <= buildQualityValue <=6:
                buildQualityDisplay = f"{buildQualityValue}/5"
            else:
                buildQualityDisplay = '999'
            rsCEA['M7D'] = str(buildQualityDisplay)
            rsCEA['M7V'] = buildQualityValue
            rsCEA['M7F'] = 0

            electricalQualityValue = pitData[analysis.pitColumns.index('electricalQuality')]
            if electricalQualityValue is None:
                electricalQualityValue = 0
                electricalQualityDisplay = '-'
            elif 1 <= electricalQualityValue <=6:
                electricalQualityDisplay = f"{electricalQualityValue}/5"
            else:
                electricalQualityDisplay = '999'
            rsCEA['M8D'] = str(electricalQualityDisplay)
            rsCEA['M8V'] = electricalQualityValue
            rsCEA['M8F'] = 0

            robotDurabilityValue = pitData[analysis.pitColumns.index('robotDurability')]
            if robotDurabilityValue is None:
                robotDurabilityValue = 0
                robotDurabilityDisplay = '-'
            elif 1 <= robotDurabilityValue <=6:
                robotDurabilityDisplay = f"{robotDurabilityValue}/5"
            else:
                robotDurabilityDisplay = '999'
            rsCEA['M9D'] = str(robotDurabilityDisplay)
            rsCEA['M9V'] = robotDurabilityValue
            rsCEA['M9F'] = 0
        
    return rsCEA