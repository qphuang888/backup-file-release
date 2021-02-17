import sys
from backupFileModule import BackupFileModule

if __name__ == '__main__':
    backup = BackupFileModule(sys.argv[1], sys.argv[2])
    backup.run()

