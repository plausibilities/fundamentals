import pymc3 as pm
import graphviz


class Characteristics:

    def __init__(self, model, trace):
        """

        :param model:
        :param trace:
        """

        self.model: pm.Model = model
        self.trace: pm.backends = trace

    def trace_(self, coordinates, lines: bool):
        """
        
        :param coordinates:
        :param lines:
        :return:
        """

        if lines:
            with self.model:
                pm.traceplot(data=self.trace, figsize=coordinates.figsize,
                             var_names=coordinates.var_names,
                             lines=coordinates.lines)
        else:
            with self.model:
                pm.traceplot(data=self.trace, figsize=coordinates.figsize,
                             var_names=coordinates.var_names)

    def dag_(self, path: str, display: bool = False):
        """

        :param path: A path, and file, name for the hypothesis model diagram being rendered, excluding an extension
        :param display: Should the diagram be displayed within Jupyter?
        :return:
        """

        pathstr = path + '.gv'

        # Render the hypothesis model and save it
        diagram = pm.model_graph.ModelGraph(model=self.model).make_graph()
        diagram.node_attr.update(shape='circle')
        diagram.save(filename=pathstr)

        # Render and save the PDF form of the model
        graphviz.render(engine='dot', format='pdf', filepath=pathstr)

        # View the model within Jupyter?
        if display:
            graphviz.Source.from_file(filename=pathstr)
