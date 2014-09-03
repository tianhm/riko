# Pipe pipe_6e30c269a69baf92cd420900b0645f88 generated by pipe2py

from pipe2py import Context
from pipe2py.modules.pipeforever import pipe_forever
from pipe2py.modules.pipefetch import pipe_fetch
from pipe2py.modules.pipefetch import pipe_fetch
from pipe2py.modules.pipeunion import pipe_union
from pipe2py.modules.pipeuniq import pipe_uniq
from pipe2py.modules.pipefilter import pipe_filter
from pipe2py.modules.piperename import pipe_rename
from pipe2py.modules.piperegex import pipe_regex
from pipe2py.modules.pipesort import pipe_sort
from pipe2py.modules.pipeoutput import pipe_output

def pipe_6e30c269a69baf92cd420900b0645f88(context=None, _INPUT=None, conf=None, **kwargs):
    # todo: insert pipeline description here
    conf = conf or {}

    if context.describe_input:
        return []

    forever = pipe_forever()


    sw_135 = pipe_fetch(
        context, forever, conf=dict(URL=dict(type='url', value='file://data/rss.sueddeutsche.de_rss_Topthemen.xml')))

    sw_233 = pipe_fetch(
        context, forever, conf=dict(URL=dict(type='url', value='file://data/rss.sueddeutsche.de_rss_Politik.xml')))

    sw_154 = pipe_union(
        context, forever, _OTHER3=sw_233, conf=dict(), _OTHER=sw_135)

    sw_173 = pipe_uniq(
        context, sw_154, conf=dict(field=dict(type='text', value='title')))

    sw_180 = pipe_filter(
        context, sw_173, conf=dict(COMBINE=dict(type='text', value='or'), MODE=dict(type='text', value='block'), RULE=[dict(field=dict(type='text', value='link'), value=dict(type='text', value='/sport/'), op=dict(type='text', value='contains')), dict(field=dict(type='text', value='title'), value=dict(type='text', value='Bildstrecke:'), op=dict(type='text', value='contains'))]))

    sw_210 = pipe_rename(
        context, sw_180, conf=dict(RULE=[dict(newval=dict(type='text', value='link'), field=dict(type='text', value='y:id.value'), op=dict(type='text', value='copy'))]))

    sw_195 = pipe_regex(
        context, sw_210, conf=dict(RULE=[dict(singlelinematch=dict(type='text', value='2'), globalmatch=dict(type='text', value='1'), replace=dict(type='text', value=''), field=dict(type='text', value='description'), match=dict(type='text', value='</div>.*$'), casematch=dict(type='text', value='8')), dict(field=dict(type='text', value='link'), match=dict(type='text', value='^(.*\\/.*)\\/'), replace=dict(type='text', value='$1/2.220/'))]))

    sw_191 = pipe_sort(
        context, sw_195, conf=dict(KEY=[dict(field=dict(type='text', value='pubDate'), dir=dict(type='text', value='DESC'))]))

    _OUTPUT = pipe_output(
        context, sw_191, conf=dict())

    return _OUTPUT


if __name__ == "__main__":
    context = Context()
    pipeline = pipe_6e30c269a69baf92cd420900b0645f88(context, None)

    for i in pipeline:
        print i