from typing import List, Optional

class Project:
    def __init__(
        self, 
        locator: str, 
        title: str, 
        description: Optional[str] = None, 
        public: Optional[bool] = None, 
        policyId: Optional[int] = None, 
        securityPolicyId: Optional[int] = None, 
        qualityPolicyId: Optional[int] = None, 
        authors: Optional[List[str]] = None, 
        organizationId: Optional[int] = None, 
        last_analyzed_revision: Optional[str] = None, 
        issue_tracker_url: Optional[str] = None, 
        issue_tracker_id: Optional[str] = None, 
        issue_tracker_type: Optional[str] = None, 
        createdAt: Optional[str] = None, 
        updatedAt: Optional[str] = None, 
        revisions: Optional[List] = None
    ):
        self.locator = locator
        self.title = title
        self.description = description
        self.public = public
        self.policyId = policyId
        self.securityPolicyId = securityPolicyId
        self.qualityPolicyId = qualityPolicyId
        self.authors = authors if authors is not None else []
        self.organizationId = organizationId
        self.last_analyzed_revision = last_analyzed_revision
        self.issue_tracker_url = issue_tracker_url
        self.issue_tracker_id = issue_tracker_id
        self.issue_tracker_type = issue_tracker_type
        self.createdAt = createdAt
        self.updatedAt = updatedAt
        self.revisions = revisions if revisions is not None else []