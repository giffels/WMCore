#!/usr/bin/env python
"""
_Save_

MySQL implementation of BossLite.Jobs.Save
"""

__all__ = []

from WMCore.Database.DBFormatter import DBFormatter
from WMCore.BossLite.DbObjects.Job import JobDBFormatter

class Save(DBFormatter):
    """
    BossLite.Jobs.Save
    """
    
    sql = """UPDATE bl_job SET job_id = :jobId, task_id = :taskId, 
                wmbs_job_id = :wmbsJobId, name = :name, 
                executable = :executable, events = :events,
                arguments = :arguments, stdin = :standardInput,
                stdout = :standardOutput, stderr = :standardError,
                input_files = :inputFiles, output_files = :outputFiles,
                output_dir = :outputDirectory, 
                dls_destination = :dlsDestination, 
                submission_number = :submissionNumber, closed = :closed
                WHERE job_id = :jobId AND task_id = :taskId
                """
    
    def execute(self, binds, conn = None, transaction = False):
        """
        execute
        """
        
        objFormatter = JobDBFormatter()
        
        ppBinds = objFormatter.preFormat(binds)
        
        self.dbi.processData(self.sql, ppBinds, conn = conn,
                         transaction = transaction)
        
        # try to catch error code?
        return

