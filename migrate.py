import alembic.config


def upgrade(revision='head'):
    upgrade_args = [
        '--raiseerr',
        'upgrade',
        revision,
    ]

    alembic.config.main(argv=upgrade_args)

def downgrade(revision):
    downgrade_args = [
        '--raiseerr',
        'downgrade',
        revision
    ]
    alembic.config.main(argv=downgrade_args)


if __name__ == '__main__':
    upgrade()
