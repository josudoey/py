from oslo.config import cfg
CONF = cfg.CONF

cli_opts = [
    cfg.BoolOpt('verbose',
    short='v', default=False, help='Print more verbose output'),
    cfg.BoolOpt('debug',
        short='d', default=False, help='Print debugging output'),
]
CONF.register_cli_opts(cli_opts)

