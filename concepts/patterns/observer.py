from datetime import datetime
from abc import abstractmethod


class Observer:
    def __init__(self):
        pass

    @abstractmethod
    def update(self, event_data):
        pass


class Subject:
    def __init__(self):
        self._observers: list[Observer] = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, event_data):
        for observer in self._observers:
            observer.update(event_data)


class WorkflowEngine(Subject):
    def __init__(self):
        super().__init__()
        self.status = "idle"

    def start_workflow(self, workflow_id):
        self.status = "running"
        self.notify({
            'event': 'workflow_started',
            'workflow_id': workflow_id,
            'timestamp': datetime.now()
        })

    def complete_workflow(self, workflow_id):
        self.status = "completed"
        self.notify({
            'event': 'workflow_completed',
            'workflow_id': workflow_id,
            'timestamp': datetime.now()
        })


# Observers
class EmailNotifier(Observer):
    def update(self, event_data):
        print(f"Email: Workflow {event_data['workflow_id']} - {event_data['event']}")


class SlackNotifier(Observer):
    def update(self, event_data):
        print(f"Slack: Workflow {event_data['workflow_id']} - {event_data['event']}")


class AuditLogger(Observer):
    def update(self, event_data):
        print(f"Audit: {event_data['event']} at {event_data['timestamp']}")


# Usage
workflow_engine = WorkflowEngine()
workflow_engine.attach(EmailNotifier())
workflow_engine.attach(SlackNotifier())
workflow_engine.attach(AuditLogger())

workflow_engine.start_workflow("WF-001")
