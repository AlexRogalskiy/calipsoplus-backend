class QuotaExceptionExceeded(Exception):
    pass


class QuotaMaxSimultaneousExceeded(QuotaExceptionExceeded):
    pass


class QuotaCpuExceeded(QuotaExceptionExceeded):
    pass


class QuotaMemoryExceeded(QuotaExceptionExceeded):
    pass


class QuotaHddExceeded(QuotaExceptionExceeded):
    pass


class DockerExceptionNotFound(Exception):
    pass
