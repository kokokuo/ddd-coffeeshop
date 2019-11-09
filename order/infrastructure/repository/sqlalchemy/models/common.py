from datetime import datetime
from order.infrastructure.repository.sqlalchemy import dbo


class SystemInfo(dbo.Model):
    # Abstract Model , for every model used
    __abstract__ = True

    # utc get utf time, if need local time, please call now()
    created_at = dbo.Column(dbo.DateTime,
                            default=datetime.utcnow,
                            nullable=False)
    modified_at = dbo.Column(dbo.DateTime,
                             onupdate=datetime.utcnow,
                             nullable=True)
    deleted_at = dbo.Column(dbo.DateTime, nullable=True)
    # mark data was deleted
    mark_deleted = dbo.Column(dbo.Boolean, default=False, nullable=False)
    # who operating this data
    operate_account = dbo.Column(dbo.String(40), nullable=True)

    def __init__(self, **kwargs):
        for key, val in kwargs.items():
            setattr(self, key, val)

    def __repr__(self):
        print("<SystemInfo: \n\
            created_at:%s\n\
            modified_at=%s\n\
            deleted_at=%s\n\
            mark_deleted=%s\n\
            operate_account=%s>" % (self.created_at,
                                    self.modified_at,
                                    self.deleted_at,
                                    self.mark_deleted,
                                    self.operate_account))
